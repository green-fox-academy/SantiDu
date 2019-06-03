import json, re
from collections import namedtuple
from datetime import datetime

with open("thanks_channel.json", encoding="UTF8") as f:
    msges = json.load(f)

Message = namedtuple("Message", "msg_id text user_id subtype posttime is_parent_thread edit_time")
Reaction = namedtuple("Reaction", "msg_id, user_id reaction")
Mention = namedtuple("Mention", "msg_id user_id")

user_pattern_in_mention = re.compile("(?<=<@).{9}(?=>)")

def parse_slack(msges):
    for msg in msges:
        msg_id = msg["ts"]
        text = msg["text"]
        user_id = msg.get("user")
        subtype = msg.get("subtype")
        posttime = datetime.utcfromtimestamp(float(msg_id)).strftime('%Y-%m-%d %H:%M:%S')
        is_parent_thread = (True if msg.get("thread_ts") and msg["thread_ts"] == msg["ts"] else None)
        if msg.get("edited"):
            edit_time = datetime.utcfromtimestamp(float(msg["edited"]["ts"])).strftime('%Y-%m-%d %H:%M:%S')
        else:
            edit_time = None
        output_message = Message(msg_id=msg_id, text=text, user_id=user_id, subtype=subtype, posttime=posttime, 
                          is_parent_thread=is_parent_thread, edit_time=edit_time)
        output_reactions = ()
        reactions = msg.get("reactions")
        if reactions:
            for reaction in reactions:
                for user in reaction["users"]:
                    output_reactions = output_reactions + (Reaction(msg_id=msg_id, user_id=user, reaction=reaction["name"]),)
        output_mentions = ()
        for user in user_pattern_in_mention.findall(text):
            output_mentions = output_mentions + (Mention(msg_id=msg_id, user_id=user),)
        yield output_message, output_reactions, output_mentions

data = parse_slack(msges)

msg_tuple = ()
reaction_tuple = ()
mention_tuple = ()

while True:
    try:
        msg, reactions, mentions = next(data)
        msg_tuple = msg_tuple + (msg,)
        reaction_tuple = reaction_tuple + reactions
        mention_tuple = mention_tuple + mentions
    except StopIteration:
        break