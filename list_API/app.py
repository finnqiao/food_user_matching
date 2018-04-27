#!/usr/bin/env python
# #!flask/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
#
user = {
    'gender': 'Male',
    'age': 2,
    'knowledge': 4,
    'budget': 2,
    'dietary': {
        "None": 1,
        "Vegan": 0,
        "Vegetarian": 0,
        "Pescatarian": 0
    },
    'allergies': {
        'Peanut':0,
        'Tree Nuts':0,
        'Milk':1,
        'Egg':0,
        'Wheat':0,
        'Soy':1,
        'Fish':0,
        'Shellfish':0,
        'Meat':0,
        'Poultry':0
    },
    'location': {
        'neighborhood': 'SOMA',
        'latitude':37.7785189,
        'longitude':-122.4056395
    },
    'curLocation': {
        'latitude':37.771741,
        'longitude':-122.409281
    },
    'cuisines': {
        'African':0,
        'American':0,
        'Chinese':1,
        'Thai':0,
        'Japanese':0,
        'Korean':1,
        'Vietnamese':0,
        'Indian':0,
        'Middle Eastern':1,
        'French':0,
        'Italian':1,
        'Mexican':1,
        'Spanish':0,
        'Latin American':0,
        'Mediterranean':0,
        'Other Asian':0,
        'Other European':0
    },
    'popularity': 5,
    'rating': 4,
    'proximity': 2,
    'ambience': 1,
    'menu': 2
}

female =  {'african': 1.6887626262626264e-05, 'american': 0.00036931818181818181, 'chinese': 0.00027367424242424242, 'french': 0.00021609848484848486, 'indian': 0.00016628787878787877, 'italian': 0.00035340909090909091, 'japanese': 0.00022064393939393939, 'korean': 6.4962121212121211e-05, 'latin_american': 4.4044612794612797e-05, 'mediterranean': 8.8320707070707073e-05, 'mexican': 0.00032083333333333334, 'other_asian': 0.00010089962121212121, 'other_european': 0.00013582702020202022, 'spanish': 0.00010359848484848485, 'thai': 0.00016306818181818184, 'vietnamese': 0.00010056818181818182, 'middle_eastern': 2.4621212121212119e-05}
male =  {'african': 1.925014392630973e-05, 'american': 0.00042098445595854919, 'chinese': 0.00031196027633851469, 'french': 0.00024632987910189983, 'indian': 0.00018955094991364419, 'italian': 0.00040284974093264254, 'japanese': 0.00025151122625215893, 'korean': 7.4050086355785842e-05, 'latin_american': 5.0206294377278833e-05, 'mediterranean': 0.00010067645365572827, 'mexican': 0.00036571675302245248, 'other_asian': 0.00011501511226252158, 'other_european': 0.00015482872769142199, 'spanish': 0.0001180915371329879, 'thai': 0.00018588082901554404, 'vietnamese': 0.00011463730569948186, 'middle_eastern': 2.8065630397236616e-05}
age1 = {'african': 4.2541348600508897e-05, 'american': 0.00093034351145038165, 'chinese': 0.00068940839694656489, 'french': 0.00054437022900763357, 'indian': 0.00041889312977099239, 'italian': 0.00089026717557251901, 'japanese': 0.00055582061068702292, 'korean': 0.00016364503816793891, 'latin_american': 0.00011095207803223071, 'mediterranean': 0.00022248727735368955, 'mexican': 0.00080820610687022893, 'other_asian': 0.00025417461832061066, 'other_european': 0.00034215966921119593, 'spanish': 0.00026097328244274807, 'thai': 0.00041078244274809161, 'vietnamese': 0.00025333969465648852, 'middle_eastern': 6.2022900763358783e-05}
age2 = {'african': 4.2541348600508897e-05, 'american': 0.00093034351145038165, 'chinese': 0.00068940839694656489, 'french': 0.00054437022900763357, 'indian': 0.00041889312977099239, 'italian': 0.00089026717557251901, 'japanese': 0.00055582061068702292, 'korean': 0.00016364503816793891, 'latin_american': 0.00011095207803223071, 'mediterranean': 0.00022248727735368955, 'mexican': 0.00080820610687022893, 'other_asian': 0.00025417461832061066, 'other_european': 0.00034215966921119593, 'spanish': 0.00026097328244274807, 'thai': 0.00041078244274809161, 'vietnamese': 0.00025333969465648852, 'middle_eastern': 6.2022900763358783e-05}
age3 = {'african': 3.6305646036916392e-05, 'american': 0.00079397394136807812, 'chinese': 0.0005883550488599348, 'french': 0.00046457654723127041, 'indian': 0.00035749185667752447, 'italian': 0.00075977198697068401, 'japanese': 0.00047434853420195441, 'korean': 0.00013965798045602605, 'latin_american': 9.4688744118711553e-05, 'mediterranean': 0.00018987513572204127, 'mexican': 0.00068973941368078177, 'other_asian': 0.00021691775244299675, 'other_european': 0.00029200597176981541, 'spanish': 0.00022271986970684039, 'thai': 0.0003505700325732899, 'vietnamese': 0.00021620521172638436, 'middle_eastern': 5.293159609120521e-05}
age4 = {'african': 3.2306763285024153e-05, 'american': 0.00070652173913043469, 'chinese': 0.00052355072463768115, 'french': 0.00041340579710144923, 'indian': 0.00031811594202898552, 'italian': 0.0006760869565217391, 'japanese': 0.00042210144927536233, 'korean': 0.00012427536231884059, 'latin_american': 8.4259259259259251e-05, 'mediterranean': 0.00016896135265700483, 'mexican': 0.00061376811594202898, 'other_asian': 0.00019302536231884058, 'other_european': 0.00025984299516908211, 'spanish': 0.00019818840579710143, 'thai': 0.00031195652173913042, 'vietnamese': 0.00019239130434782608, 'middle_eastern': 4.7101449275362324e-05}
age5= {'african': 3.2306763285024153e-05, 'american': 0.00070652173913043469, 'chinese': 0.00052355072463768115, 'french': 0.00041340579710144923, 'indian': 0.00031811594202898552, 'italian': 0.0006760869565217391, 'japanese': 0.00042210144927536233, 'korean': 0.00012427536231884059, 'latin_american': 8.4259259259259251e-05, 'mediterranean': 0.00016896135265700483, 'mexican': 0.00061376811594202898, 'other_asian': 0.00019302536231884058, 'other_european': 0.00025984299516908211, 'spanish': 0.00019818840579710143, 'thai': 0.00031195652173913042, 'vietnamese': 0.00019239130434782608, 'middle_eastern': 4.7101449275362324e-05}
age6 = {'african': 3.4294871794871794e-05, 'american': 0.00075000000000000002, 'chinese': 0.00055576923076923078, 'french': 0.00043884615384615381, 'indian': 0.00033769230769230767, 'italian': 0.00071769230769230764, 'japanese': 0.00044807692307692306, 'korean': 0.00013192307692307692, 'latin_american': 8.9444444444444443e-05, 'mediterranean': 0.00017935897435897438, 'mexican': 0.00065153846153846165, 'other_asian': 0.00020490384615384614, 'other_european': 0.00027583333333333328, 'spanish': 0.00021038461538461537, 'thai': 0.00033115384615384615, 'vietnamese': 0.00020423076923076921, 'middle_eastern': 5.0000000000000002e-05}
know1 = {'african': 2.2793115201090661e-05, 'american': 0.0004984662576687116, 'chinese': 0.0003693762781186094, 'french': 0.00029166666666666669, 'indian': 0.00022443762781186095, 'italian': 0.00047699386503067485, 'japanese': 0.00029780163599182007, 'korean': 8.7678936605316982e-05, 'latin_american': 5.9446716655305615e-05, 'mediterranean': 0.00011920586230402181, 'mexican': 0.00043302658486707565, 'other_asian': 0.00013618353783231084, 'other_european': 0.00018332481254260396, 'spanish': 0.00013982617586912066, 'thai': 0.00022009202453987731, 'vietnamese': 0.0001357361963190184, 'middle_eastern': 3.3231083844580775e-05}
know2 = {'african': 6.1443236714975842e-05, 'american': 0.0004812047101449275, 'chinese': 0.00044067028985507245, 'french': 0.00043863224637681158, 'indian': 0.00039651268115942028, 'italian': 0.00054144021739130441, 'japanese': 0.00042368659420289852, 'korean': 0.00020538949275362322, 'latin_american': 0.00016238929146537845, 'mediterranean': 0.00020750301932367151, 'mexican': 0.00049977355072463767, 'other_asian': 0.00026358695652173915, 'other_european': 0.00029630887681159421, 'spanish': 0.00028702445652173912, 'thai': 0.0003992300724637681, 'vietnamese': 0.00027740036231884059, 'middle_eastern': 0.00010801630434782609}
know3 = {'african': 0.00022996794871794869, 'american': 0.00046634615384615383, 'chinese': 0.00040384615384615388, 'french': 0.00052884615384615383, 'indian': 0.00046153846153846158, 'italian': 0.00050000000000000001, 'japanese': 0.00043269230769230771, 'korean': 0.00035576923076923074, 'latin_american': 0.00035790598290598289, 'mediterranean': 0.00034775641025641029, 'mexican': 0.00050000000000000001, 'other_asian': 0.00038581730769230772, 'other_european': 0.00041266025641025639, 'spanish': 0.00042788461538461535, 'thai': 0.00046153846153846158, 'vietnamese': 0.00040384615384615388, 'middle_eastern': 0.00026923076923076922}
know4 = {'african': 0.00011967054263565891, 'american': 0.00046366279069767443, 'chinese': 0.00048546511627906979, 'french': 0.0005007267441860465, 'indian': 0.00049273255813953487, 'italian': 0.00057049418604651159, 'japanese': 0.00050508720930232556, 'korean': 0.00034811046511627904, 'latin_american': 0.00025750968992248059, 'mediterranean': 0.00030208333333333329, 'mexican': 0.00051526162790697678, 'other_asian': 0.00037590843023255812, 'other_european': 0.00037439437984496132, 'spanish': 0.00040225290697674422, 'thai': 0.00049709302325581393, 'vietnamese': 0.00040625000000000004, 'middle_eastern': 0.00022311046511627907}

vendors = []
with open('../vendor-data.txt') as json_data:
    d = json.load(json_data)
    vendors.append(d)

topList = ['Taqueria Angelicas', 'Modernist Spring Dinner', 'Spork & Stix', 'Mayo & Mustard', 'ICHIDO Japanese Omakase', 'Little Green Cyclo', 'Noodle in a Haystack: Paitan / Tan Tan', 'Noodle in a Haystack: Spicy Miso Paitan', 'The Art of Making Chocolate Truffles + Wine & Chocolate Pairing Flight (hands on class)', 'Istanbul Modern, Spring (10 course)']

app = Flask(__name__)
api = Api(app)

app = Flask(__name__)


@app.route('/')
def index():

    return jsonify(know4)

@app.route('/list')
def list():
    return jsonify(topList)

if __name__ == '__main__':
    app.run(debug=True)
