from django import forms

from .models import *

length = 50

class AirlineForm(forms.ModelForm):
    aname = forms.CharField(label='Air Line Name', max_length=length, required=True)
    airlinecode = forms.CharField(label='Air Line Code', max_length=5, required=True)
    description = forms.CharField(
        label='Description',
        max_length=length,
        required=False,
        widget=forms.Textarea
    
    )


    class Meta:
        model = Airline
        fields = [
            'aname',
            'airlinecode',
            'description'
        ]


class PassengerForm(forms.ModelForm):

    pname= forms.CharField( 
        max_length=length,
        required=False,
        label='Passenger Name',
        widget=forms.TextInput(
            attrs={
                'class': 'temprary'
            }
        )    
    )

    pticketno= forms.CharField( 
        max_length=length,
        required=False,
        label='Passenger Ticket No',
        widget=forms.TextInput(
            attrs={
                'class': ''
            }
        )    
    )

    pamount= forms.CharField( 
        max_length=length,
        required=False,
        label='Ticket Amount',
        widget=forms.TextInput(
            attrs={
                'class': 'ticketamount'
            }
        )    
    )

    class Meta:
        model = Passenger
        fields =[
            'pname',
            'pticketno',
            'pamount',
            'pnrfrom'
        ]



class TicketForm(forms.ModelForm):
    
    dateofissue = forms.DateField(
        required=True,
        label='Date of Issue',
        widget=forms.TextInput(
            attrs={
                'type': 'date'
            }
        )
    )

    traveldate = forms.DateField(
        required=True,
        label='Travel Date',
        widget=forms.TextInput(
            attrs={
                'type': 'date'
            }
        )
    )
    pnr = forms.CharField(
        required=True,
        label='PNR',
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )
    

    totalamount = forms.CharField(
        required=True,
        label='Total Amount',
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'readonly': 'readonly'
            }
        )
    )

    recievedamount = forms.CharField(
        required=True,
        label='Recieved Amount',
        widget=forms.TextInput(
            attrs={
                'type': 'number'
            }
        )
    )

    recieveableamount = forms.CharField(
        required=True,
        label='Recieveable Amount',
        widget=forms.TextInput(
            attrs={
                'type': 'number'
            }
        )
    )

    remainingamount = forms.CharField(
        required=True,
        label='Remaining Amount',
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'readonly': 'readonly'
            }
        )
    )

    profit = forms.CharField(
        required=True,
        label='Profit',
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'readonly': 'readonly'
            }
        )
    )
    
    

    root = forms.CharField(
        required=True,
        label='Route',
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )


    Description = forms.CharField(required=False, max_length=length, widget=forms.Textarea)

    class Meta:
        model = Ticket
        fields = [
            'dateofissue',
            'root',
            'traveldate',
            'pnr',
            'totalamount',
            'recievedamount',
            'recieveableamount',
            'remainingamount',
            'profit',
            'airline',
            'madeby',
            'careof',
            'Description'
        ]
