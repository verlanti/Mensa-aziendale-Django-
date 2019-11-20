from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .form import  PlateForm, MenuForm, OrdineForm
from .models import Plates, Employee, Day
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
####################PLATE###################################################3
#class InsertPlate(generic.CreateView):
#    form_class = PlateForm
#    template_name = 'app/insertPlate.html'
#    success_url = reverse_lazy('app:insertplate')

#    def post(self, request):
#        if request.method == 'POST':
#            form = PlateForm(request.POST)
#            if form.is_valid():
#                plate = form.save()
#                return redirect('app:insertplate')
#            else:
#                form = PlateForm()

#        return render(request, 'app/insertPlate.html', {'form': form})
################################################################################
def insertPlate(request):
    form = PlateForm()

    if request.method == 'POST':
        form = PlateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:insertplate')
        else:
            form = PlateForm()

    return render(request, 'app/insertPlate.html', {'form': form})


def changePlate(request, id):
    if request.method == 'POST':
        p = Plates.objects.get(pk=id)
        form = PlateForm(request.POST,instance=p)
        form.save()
        return redirect('app:listplate')
    else:
        p = Plates.objects.get(pk=id)
        form = PlateForm(instance = p)
        return render(request, 'app/changePlate.html', {'form': form})


def deletePlate(request, id):
    p = Plates.objects.get(pk=id)
    p.delete()
    return redirect('app:listplate')


class ListPlates(generic.ListView):
    template_name = 'app/listPlates.html'
    context_object_name = 'list_plates'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            if 'delete' in request.POST:
                key = request.POST['delete']
                return redirect('app:deleteplate', id=key)
            elif 'change' in request.POST:
                key = request.POST['change']
                return redirect('app:changeplate',id=key)


    def get_queryset(self):
        return Plates.objects.all()



#####################MENU#############################################################
class Menu(generic.ListView):
    template_name = 'app/menu.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            if 'delete' in request.POST:
                key = request.POST['delete']
                return redirect('app:deletemenu',id=key)
            elif 'change' in request.POST:
                key = request.POST['change']
                return redirect('app:changeplate',id=key)


    def get_queryset(self):
        pass


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_dict'] = { 'Primo': [] , 'Secondo': [], 'Contorno': [], 'Dessert': [] }
        for plate in Plates.objects.all():
            if plate.is_menu and plate.menu_name.name=='Primo' :
                context['menu_dict']['Primo'].append(plate)
            if plate.is_menu and plate.menu_name.name=='Secondo' :
                context['menu_dict']['Secondo'].append(plate)
            if plate.is_menu and plate.menu_name.name=='Contorno' :
                context['menu_dict']['Contorno'].append(plate)
            if plate.is_menu and plate.menu_name.name=='Dessert' :
                context['menu_dict']['Dessert'].append(plate)


        return context

#elimina solo il piatto dal menu
def deleteMenu(request,id):
    p = Plates.objects.get(pk=id)
    p.is_menu = False
    p.save()
    return redirect('app:menu')

def changeMenu(request):
        form = MenuForm()
        if request.method == 'POST':
            form = MenuForm(request.POST)
            if form.is_valid():
                menu_dict = form.cleaned_data
                #print(menu_dict)

                for key, value in menu_dict.items():
                        plate = Plates.objects.filter(name=value.name)[0]
                        if not plate.is_menu:
                            plate.is_menu = True
                            plate.save()

                return redirect('app:menu')
        else:
            form = MenuForm()
        return render(request, 'app/changeMenu.html', {'form': form})




def ordine(request):
    list_menu = Plates.objects.filter(is_menu=True)

    form = OrdineForm()
    totale = 0
    if request.method == 'POST':
        form = OrdineForm(request.POST)
        if form.is_valid():
            totale = 0
            plate_dict = form.cleaned_data['plate_chosen']
            for p in plate_dict:
                totale += p.price

            ordine = form.save(commit=False)
            ordine.save()
            form.save_m2m()

            emp = Employee.objects.latest('id')
            #print(emp)
            emp.total =  totale
            emp.name=request.user.username
            emp.save()
            return redirect('app:ordine')
    else:
        form = OrdineForm()


    return render(request, 'app/ordine.html', {'form': form, 'list_menu':list_menu})

class ListOrdini(generic.ListView):
    template_name = 'app/ordine_cuoco.html'


    def get_queryset(self):
        pass


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['list_ordini'] = { 'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],
                                  'Friday':[],'Saturday':[],'Sunday':[] }
        for day in Day.objects.all():
            context['list_ordini'][day.d].append(Employee.objects.filter(date=day.id))
        #print(context['list_ordini'])

        return context


def deleteOrdine(request, id):
    p = Employee.objects.get(pk=id)
    p.delete()
    return redirect('app:listordini')




def daily_cost(dict_spese,user,day):
    total_weekly = 0
    total = 0
    for d in day:
        for u in dict_spese.keys():
            for emp in Employee.objects.filter(name=u.username,date=d):
                total += emp.total
            dict_spese[u].append(total)
            total = 0
    for u in dict_spese.keys():
        for w in dict_spese[u]:
            total_weekly += w
        dict_spese[u].append(total_weekly)
        total_weekly= 0
    return dict_spese

def daily_chose(dict_plate_scelte,plate,day):
    total_weekly = 0
    total = 0
    for d in day:
        for p in dict_plate_scelte.keys():
            for emp in Employee.objects.filter(plate_chosen=p,date=d):
                total += 1
            dict_plate_scelte[p].append(total)
            total = 0
    for p in dict_plate_scelte.keys():
        for w in dict_plate_scelte[p]:
            total_weekly += w
        dict_plate_scelte[p].append(total_weekly)
        total_weekly= 0

    return dict_plate_scelte



# Ritorna una lista con i valori in percentuali delle scelte
def total_choose(daily_choose):
    total = 0
    for v in daily_choose.items():
         total += v[1][7]

    choose = {}
    for key,value in daily_choose.items():
        choose[key] = (value[7],round(value[7]/total*100,2))

    return choose

# Ritorna una lista con i valori in percentuali dei costi
def total_cost(daily_cost):
    total = 0
    for v in daily_cost.items():
         total += v[1][7]

    cost = {}
    for key,value in daily_cost.items():
        cost[key] = (value[7],round(value[7]/total*100,2))
    return cost


# View che tiene conto delle Statistiche
class StatisticsList(generic.ListView):
    template_name = 'app/statistiche.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
################################################################################
        user = User.objects.filter(groups__name='Impiegato')
        day = Day.objects.all()
        dict_spese = {el:[] for el in user}
        context['daily_cost'] = daily_cost(dict_spese,user,day)
        context['day'] = day
################################################################################
        plate = Plates.objects.all()
        dict_plate_scelte = {el:[] for el in plate}
        context['daily_chose'] = daily_chose(dict_plate_scelte,plate,day)

        context['total_chose'] = total_choose(context['daily_chose'])
        context['total_cost'] = total_cost(context['daily_cost'])
        context['top_3'] = []
        i=0
        for key, value in sorted(context['total_chose'].items(), key=lambda item: item[1][1],reverse=True):
            context['top_3'].append([key,value])
            if i == 2 :
                break
            i += 1
        return context
