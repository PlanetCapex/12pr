import mathplotlib.pyplot as plt
import os
import io
import requests

def get_data(array, name):
    arr = {}
    for record in array:
        arr.append(record[name])
    return arr

def open_graph(folder):
    file = open(folder + "/analitic.png")
    bytes_file = io.BytesIO(file)
    return bytes_file

def find_graph(array):
    folder = f"upload/{array[0]['date']}_{array[len(array)-1]['date']}_{array[0]['subject']}"
    if os.path.isdir(folder):
        return open_graph(folder)
    else:
        return create_graph(array, folder)

def create_graph(array, folder):
    x = get_data(array, 'markValue')
    ny = get_data(array, 'markSetDate')
    y = {}
    for record in ny:
        y += '-'.join(record)
    plt.plot(x, y, color='blue', marker='o', marksize=7)
    plt.xlablel('Оценка')
    plt.ylablel('Дата')
    payload = {'id': array[0]['subject']}
    url = os.environ.get('MAINHOST') +'/api/subjects/'
    r = requests.get(url, params=payload)
    subject = r.json()
    plt.title(subject['name'])
    plt.savefig(folder+'/analitic.png')
    plt.close()
    return open_graph(folder)
    


    