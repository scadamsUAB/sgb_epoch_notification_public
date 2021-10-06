import requests



def sendMessage(token, channel_id, message):
    url ="https://discord.com/api/v8/channels/"+str(channel_id)+"/messages" 
    header ={"authorization": token}
    data = {"content": message}
    
    requests.post(url,data = data, headers = header)


def multi_send(token, message,channels):
    for c in channels:
        sendMessage(token,c["channel_id"],message)