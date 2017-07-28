
def globals(request):
    #import pdb
    #pdb.set_trace()
    data = {}

    if 'menu_item' in request.session:
        data['menu_item'] = request.session['menu_item']

    return data
