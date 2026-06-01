import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

#encode (text -> token IDs)
x= enc.encode("hellon world")
print(x)  #[15339,1917] <- token ids

#dcode(token IDs -> text)
y= enc.decode(x)
print(y)  # "hello world"

# apde aek word nakhyo aeni pachi ni najik kya ave ae ape aene vector kevay