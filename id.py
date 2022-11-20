import requests

def id_counter():

    n = requests.get('https://www.youtube.com/channel/UC5WRs--U1i_ka7U4W4_du8A').text
    with open("url.txt", "w") as file:
        file.write(n)




    f = n.find(' подписчик')

    n = n[f-2:f+10]

    n = list(map(str, n.split()))[0]

    return n

print(id_counter())