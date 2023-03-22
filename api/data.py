""""random api data"""
import uuid
import datetime

data = {
 
    'restaurants':[
        {
            'id':uuid.uuid4(),
            'name':'friends of christ',
            'description':'test at it fullest',
            'location':'kampala, Uganda',
            'Is_operational':True,
            'order_fullfilling':'True',
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(), 
            'products':[
                {},
                {},
                {}
                ],
            'menus':[
                {},
                {},
                {}
            ]
            
        },
        {
            'id':uuid.uuid4(),
            'name':'Nile restuarant',
            'description':'Feel the test of the Nile',
            'location':'Egypt, Cairo',
            'Is_operational':True,
            'order_fullfilling':'True',
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(), 
            'products':[
                {},
                {},
                {}
                ],
            'menus':[
                {},
                {},
                {}
            ]
                                
        },
        {
            'id':uuid.uuid4(),
            'name':'KFC',
            'description':'Chicken is our thing',
            'location':'Lome, Togo',
            'Is_operational':True,
            'order_fullfilling':'True',
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(), 
            'products':[
                {},
                {},
                {}
                ],
            'menus':[
                {},
                {},
                {}
            ]
        },
        {
          'id':uuid.uuid4(),
            'name':'The Terrance',
            'description':'Feel the fresh Treats from Our Cusines',
            'location':'kampala, Uganda',
            'Is_operational':True,
            'order_fullfilling':'True',
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(), 
            'products':[
                {},
                {},
                {}
                ],
            'menus':[
                {},
                {},
                {}
            ]
              
        },
        {
            'id':uuid.uuid4(),
            'name':'Hillton Urban Restaurant',
            'description':'Marriot is our way',
            'location':'Nariobi, Kenya',
            'Is_operational':True,
            'order_fullfilling':'True',
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(), 
            'products':[
                {},
                {},
                {}
                ],
            'menus':[
                {},
                {},
                {}
            ]
            }],
    'users':[],
    'orders':[],
    'menus':[],
    'menu_items':[],
    'checkouts':[],
    'addresses':[],
    'payments':[],
    'shipments':[],
    'transactions':[],
    'reservations':[],
    'products':[],
    'product_categories':[],
    
}
