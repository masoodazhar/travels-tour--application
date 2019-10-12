from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
# Create your views here.


def ticketadd(request):
    if request.method=='POST':
        
        # ticketform = TicketForm(request.POST)

        ticketformd = Ticket(
            dateofissue=request.POST.get('dateofissue'),
            root = request.POST.get('root'),
            traveldate = request.POST.get('traveldate'),
            pnr = request.POST.get('pnr'),
            totalamount = request.POST.get('totalamount'),
            recievedamount = request.POST.get('recievedamount'),
            recieveableamount = request.POST.get('recieveableamount'),
            remainingamount = request.POST.get('remainingamount'),
            profit = request.POST.get('profit'),
            airline = Airline.objects.get(pk=request.POST.get('airline')),
            madeby = request.POST.get('madeby'),
            careof = Customer.objects.get(pk=request.POST.get('careof')),
            Description = request.POST.get('Description')
            )
        ticketform = TicketForm(request.POST)
        # passengerform = PassengerForm(request.POST)
        
        if ticketform.is_valid():
            ticketformd.save()
            
            passengerformsave = request.POST
            if passengerformsave.get('range'):
                ranges =  int(passengerformsave.get('range'))
            else:
                ranges = 0;
                
            print("===============START==================")
            print(ranges)
            for cols in range(0,ranges+1):
                pnames = ''
                pticketno = ''
                pticketamount = ''
                if cols <1:
                    pticketno = 'pticketno'
                    pnames = 'pname'
                    pticketamount = 'pamount'
                else:
                    pticketno = f'pticketno{cols}'
                    pticketamount = f'pamount{cols}'
                    pnames = f'pname{cols}'
                pasname = passengerformsave.get(pnames)
                passtno = passengerformsave.get(pticketno)
                passamount = passengerformsave.get(pticketamount)
                passengerform = Passenger(pname=pasname, pticketno=passtno, pamount=passamount,pnrfrom= passengerformsave.get('pnr'))
                passengerform.save();
                # print(passengerformsave)
                # for p in passengerformsave
                # passenger(pname=passengerformsave.get(passenger), )

            print("===============END==================")

            messages.success(request,'ticket has been saved!')
            return redirect('ticketadd')
    else:
         ticketform = TicketForm()
         

    passengerform = PassengerForm()
    ticketdata = Ticket.objects.all()
    passengerdatacount = Passenger.objects.all().count()

    explodedata = []
    for i in ticketdata:
        explodedata.append({'pk':i.pk, 'totalamount': i.totalamount, 'recievedamount': i.recievedamount, 'remainingamount': i.remainingamount ,'customer': i.careof ,'pnr': i.pnr, 'PROFIT': i.profit, 'passnger': Passenger.objects.values('pnrfrom').filter(pnrfrom=i.pnr).count()})

    print(explodedata)
    context = {
        'ticketform': ticketform,
        'ticketdata': explodedata,
        'passengerform': passengerform,
        'passengerdatacount': passengerdatacount
    }
    return render(request,'ticket/index.html', context)


def ticketedit(request, pk):
    ticket_data = Ticket.objects.get(pk=pk)
    if request.method=='POST':
        ticketform = TicketForm(request.POST, instance=ticket_data)
        if ticketform.is_valid():
            ticketform.save()
            messages.success(request,'ticket has been Modified!')
            return redirect('ticketadd')
    else:
         ticketform = TicketForm(instance=ticket_data)

    ticketdata = Ticket.objects.all()
    context = {
        'ticketform': ticketform,
        'ticketdata': ticketdata
    }
    return render(request,'ticket/index.html', context)


def ticketdelete(request, pk):
     ticket_data = Ticket.objects.get(pk=pk)
     ticket_data.delete()
     messages.success(request,'ticket has been Deleted!')
     return redirect('ticketadd')


def ticketview(request, pk, pnr):
    ticketdata = Ticket.objects.filter(pk=pk).first()
    passengerdata = Passenger.objects.filter(pnrfrom=pnr)
    context = {
        'ticketdata': ticketdata,
        'passengerdata': passengerdata
    }
    return render(request,'ticket/view.html', context)


def airlineadd(request):
    if request.method=='POST':
        airlineform = AirlineForm(request.POST)
        if airlineform.is_valid():
            airlineform.save()
            messages.success(request,'airline has been saved!')
            return redirect('airlineadd')
    else:
         airlineform = AirlineForm()

    airlinedata = Airline.objects.all()
    context = {
        'airlineform': airlineform,
        'airlinedata': airlinedata
    }
    return render(request,'ticket/airline.html', context)


def airlineedit(request, pk):
    airline_data = Airline.objects.get(pk=pk)
    if request.method=='POST':
        airlineform = AirlineForm(request.POST, instance=airline_data)
        if airlineform.is_valid():
            airlineform.save()
            messages.success(request,'airline has been Modified!')
            return redirect('airlineadd')
    else:
         airlineform = AirlineForm(instance=airline_data)

    airlinedata = Airline.objects.all()
    context = {
        'airlineform': airlineform,
        'airlinedata': airlinedata
    }
    return render(request,'ticket/airline.html', context)


def airlinedelete(request, pk):
     airline_data = Airline.objects.get(pk=pk)
     airline_data.delete()
     messages.success(request,'airline has been Deleted!')
     return redirect('airlineadd')