from crud import serialize  # Import the serialize module from the crud package
from crud.models import DetailsModel  # Import the DetailsModel from the crud.models module
from crud.serialize import DetailsSerializer  # Import the DetailsSerializer from the crud.serialize module
from rest_framework.views import APIView  # Import APIView from Django REST framework
from rest_framework.response import Response  # Import Response from Django REST framework

# View for handling operations related to DetailsModel
class DetailsTable(APIView):
    def get(self, request):
        # Handle GET request to retrieve all instances of DetailsModel
        detailsObj = DetailsModel.objects.all()  # Query all records from DetailsModel
        dlSerializeObj = DetailsSerializer(detailsObj, many=True)  # Serialize the queryset
        return Response(dlSerializeObj.data)  # Return serialized data in the response

    def post(self, request):
        # Handle POST request to create a new instance of DetailsModel
        serializeobj = DetailsSerializer(data=request.data)  # Deserialize the input data
        if serializeobj.is_valid():  # Validate the deserialized data
            serializeobj.save()  # Save the new instance to the database
            return Response(status=200)  # Return a success response
        return Response(serializeobj.errors)  # Return validation errors if any


# View for deleting an existing DetailsModel instance
class DetailsDelete(APIView):
    def post(self, request, pk):
        try:
            detailObj = DetailsModel.objects.get(pk=pk)  # Retrieve the instance by primary key
        except DetailsModel.DoesNotExist:
            return Response("Not Found in Database", status=404)  # Return 404 if not found

        detailObj.delete()  # Delete the instance from the database
        return Response(status=200)  # Return a success response
    
# View for updating an existing DetailsModel instance
class DetailsUpdate(APIView):
    def post(self, request, pk):
        try:
            detailObj = DetailsModel.objects.get(pk=pk)  # Retrieve the instance by primary key
        except DetailsModel.DoesNotExist:
            return Response("Not Found in Database", status=404)  # Return 404 if not found

        serializeobj = DetailsSerializer(detailObj, data=request.data)  # Deserialize the input data for the instance
        if serializeobj.is_valid():  # Validate the deserialized data
            serializeobj.save()  # Save the updated instance to the database
            return Response(status=200)  # Return a success response
        return Response(serializeobj.errors)  # Return validation errors if any
