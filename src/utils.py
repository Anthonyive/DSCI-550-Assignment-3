import json

def jsonParser(j):
    for email in j:
        for k,v in email.items():
            if type(v) != str:
                continue
            try:
                num = float(v)
                email[k] = num
            except ValueError:
                pass

            # if the item is essentially an array:
            if len(v) >=2 and v[0] == '[' and v[-1] == ']':
                email[k] = json.loads(v.replace("\'","\""))

    return j
