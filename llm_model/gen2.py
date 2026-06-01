# ama loop lagava nu karan 3 var puchi sarkiye aek var ni badle .
from openai import OpenAI

# chatgpt na version che token upar use thay.
api_key="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" 

#OpenAI ae library client ma store karavi .
client = OpenAI(
    api_key = api_key
)

#system according answer avse input leta  matlab pela sysetm ma code nakhyo atle .
#messages list conversation history store કરે છે.

message= [                 
    {
        "role" : "system" ,
        "content" : "you are a helpful assistant."
    }
]


# 3 var mare ansewer alag rite levdavo che atle for loop use thay .
# # ne ama user according bane ne ae according answer ape.

for i in range(3):
    user_input = input("user:")
    message.append({
        "role":"user" ,                                            # message is key. 
        "content": user_input
    })                                                           #Conversation history માં user નો પ્રશ્ન add થાય છે.
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",      
        messages = message                                        # response save thase message ma thi messages માં આખી conversation જાય છે..
    )
    # have aa system ne me assistan banavyo ke tu have mari sathe work kar . 
    
    assistant_response = response.choices[0].message.content
    print("Assistant:", assistant_response)
    message.append(
        {
            "role" : "assistant",
            "content" : assistant_response
        }
    )
