from .models import Schedule
from .serializers import ScheduleSerializer, ScheduleDetailSerializer, ScheduleInputSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsSuperuserOrOwner
# import smtplib
# from email.message import EmailMessage
# from accounts.models import Account
# from properties.models import Property
# from datetime import datetime


class ScheduleCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleInputSerializer
    lookup_url_kwarg = "property_id"
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        request.data["account"] = request.user.id
        request.data["property"] = kwargs["property_id"]
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Envio de email
        # client = Account.objects.filter(id=serializer.data['account'])
        # locality = Property.objects.filter(id=serializer.data['property'])
        # EMAIL_ADRESS = 'agendamento.desa@gmail.com'
        # EMAIL_PASSWORDS = 'mwzeqpfkytrvudqj'
        # msg = EmailMessage()
        # msg['Subject'] = 'Novo agendamento realizado'
        # msg['From'] = 'agendamento.desa@gmail.com'
        # msg['To'] = client[0].email
        # if client[0].email != 'odairodriguez@yahoo.com.br':
        #     msg['Bcc'] = 'odairodriguez@yahoo.com.br'
        # day = datetime.strptime(
        #     serializer.data['date'], '%Y-%m-%d').strftime("%d/%m/%Y")
        # msg.set_content(
        #     f"Imóvel: {locality[0].enterprise} \nDia: {day} \nHorário: {serializer.data['hour']} \nCliente: {client[0].name} \nTelefone do Cliente: {client[0].phone} \nE-mail: {client[0].email}"
        # )
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     smtp.login(EMAIL_ADRESS, EMAIL_PASSWORDS)
        #     smtp.send_message(msg)
        # Final do envio de email

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ScheduleListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    http_method_names = ["get"]

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Schedule.objects.filter(account=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ScheduleDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuserOrOwner]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleDetailSerializer
    lookup_url_kwarg = "schedule_id"
    http_method_names = ["get", "patch", "delete"]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        # Envio de email
        # client = Account.objects.filter(name=serializer.data['account'])
        # EMAIL_ADRESS = 'agendamento.desa@gmail.com'
        # EMAIL_PASSWORDS = 'mwzeqpfkytrvudqj'
        # msg = EmailMessage()
        # msg['Subject'] = 'Alteração de agendamento'
        # msg['From'] = 'agendamento.desa@gmail.com'
        # msg['To'] = 'odairodriguez@yahoo.com.br'
        # day = datetime.strptime(
        #     serializer.data['date'], '%Y-%m-%d').strftime("%d/%m/%Y")
        # msg.set_content(
        #     f"Imóvel: {serializer.data['property']} \nDia: {day} \nHorário: {serializer.data['hour']} \nCliente: {client[0].name} \nTelefone do Cliente: {client[0].phone} \nE-mail: {client[0].email}"
        # )
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     smtp.login(EMAIL_ADRESS, EMAIL_PASSWORDS)
        #     smtp.send_message(msg)
        # Final do envio de email

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Envio de email
        # client = Account.objects.filter(id=instance.account_id)
        # locality = Property.objects.filter(id=instance.property_id)
        # EMAIL_ADRESS = 'agendamento.desa@gmail.com'
        # EMAIL_PASSWORDS = 'mwzeqpfkytrvudqj'
        # msg = EmailMessage()
        # msg['Subject'] = 'Exclusão de agendamento'
        # msg['From'] = 'agendamento.desa@gmail.com'
        # msg['To'] = 'odairodriguez@yahoo.com.br'
        # currency_day = f"{instance.date}"
        # day = datetime.strptime(
        #     currency_day, '%Y-%m-%d').strftime("%d/%m/%Y")
        # msg.set_content(
        #     f"******************************************** \nO AGENDAMENTO ABAIXO FOI DELETADO ******************************************** \n\n Imóvel: {locality[0].enterprise} \nDia: {day} \nHorário: {instance.hour} \nCliente: {client[0].name} \nTelefone do Cliente: {client[0].phone} \nE-mail: {client[0].email} \n--------------------------------------------------------------------\nUsuário que realizou a exclusão: \n{request.user.name}"
        # )
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     smtp.login(EMAIL_ADRESS, EMAIL_PASSWORDS)
        #     smtp.send_message(msg)
        # Final do envio de email

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
