auth = 'authentication'
order = 'order'
payment = 'payment'

auth_app = {
    'account': auth+'.Account',
    'hair_profile': auth+'.HairProfile',
}

common_model = auth+'.CommonModel'


model_app = {
    'account': auth+'.Account',
    'hair_profile': auth+'.HairProfile',
    'service': auth+'.Service',
    'artist': order+'.Artist',
    'order': order+'.OrderDetail',
    'book_service': order+'.BookService',
    'card_management': payment+'.CardManagement',
    'review': payment+'.Review',
    'payment': payment+'.Payment',
}


order = {
    'artist': order+'.Artist',
    'order': order+'.OrderDetail'
}
