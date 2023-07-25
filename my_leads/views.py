from django.shortcuts import render
from .models import *
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import File, Leads
from .serializers import LeadSerializer
# Create your views here.


#  thius side csv flie save in database
def csv_creat(file_path):
    df = pd.read_csv(file_path,decimal=',')
    print(df.values)
    csv_data = [list(row) for row in df.values]
    
    for i in csv_data:
        Leads.objects.create(
            first_name = i[0],
            last_name = i[1],
            email = i[2],
            gender = i[3],
            ip_address = i[4],
            address = i[5],
        )

def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        csv_d = File.objects.create(file= file)
        csv_creat(csv_d.file)
    return render(request, 'main.html')






# Api Create Hear
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_staff

class LeadListCreateView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        csv_data = pd.read_csv(file, decimal=',')
        leads = []
        for _, row in csv_data.iterrows():
            lead_data = {
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'gender': row['gender'],
                'ip_address': row['ip_address'],
                'address': row['address'],
            }
            leads.append(Leads(**lead_data))
        Leads.objects.bulk_create(leads)
        return Response({'message': 'Leads created successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        if user.is_staff:
            leads = Leads.objects.all()
        else:
            leads = Leads.objects.filter(assigned_to=user)
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)


