# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from django.utils import timezone
# from .models import Progress
# from .serializers import ProgressSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class ProgressView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ProgressSerializer

#     def get(self, request, *args, **kwargs):
#         user = request.user
#         date_str = request.query_params.get("date")

#         if date_str:
#             try:
#                 date_obj = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
#                 progresses = Progress.objects.filter(user=user, date=date_obj)
#             except ValueError:
#                 return Response(
#                     {"error": "Date must be in format YYYY-MM-DD"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#         else:
#             progresses = Progress.objects.filter(user=user)

#         serializer = self.get_serializer(progresses, many=True)
#         return Response(serializer.data)



#         def post(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)  # <-- hna user kayt3amer automatiquement
#         return Response(
#             {"message": "Progress created successfully", "data": serializer.data},
#             status=status.HTTP_201_CREATED,
#         )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     # def post(self, request, *args, **kwargs):
#     #     data = request.data.copy()
#     #     data["user"] = request.user.id

#     #     serializer = self.get_serializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(
#     #             {"message": "Progress created successfully", "data": serializer.data},
#     #             status=status.HTTP_201_CREATED,
#     #         )

#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         progress_id = request.data.get("id")

#         if not progress_id:
#             return Response(
#                 {"error": "You must provide an ID to update progress"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         try:
#             progress = Progress.objects.get(id=progress_id, user=request.user)
#         except Progress.DoesNotExist:
#             return Response(
#                 {"error": "Progress not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         serializer = self.get_serializer(progress, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {"message": "Progress updated", "data": serializer.data},
#                 status=status.HTTP_200_OK,
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         progress_id = request.data.get("id")

#         if not progress_id:
#             return Response(
#                 {"error": "You must provide an ID to delete progress"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         try:
#             progress = Progress.objects.get(id=progress_id, user=request.user)
#             progress.delete()
#             return Response({"message": "Progress deleted"}, status=status.HTTP_200_OK)
#         except Progress.DoesNotExist:
#             return Response(
#                 {"error": "Progress not found"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Progress
from .serializers import ProgressSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProgressView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProgressSerializer

    # GET all progresses or by date
    def get(self, request, *args, **kwargs):
        user = request.user
        date_str = request.query_params.get("date")

        if date_str:
            try:
                date_obj = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
                progresses = Progress.objects.filter(user=user, date=date_obj)
            except ValueError:
                return Response(
                    {"error": "Date must be in format YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            progresses = Progress.objects.filter(user=user)

        serializer = self.get_serializer(progresses, many=True)
        return Response(serializer.data)

    # POST new progress
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # user automatically assigned
            return Response(
                {"message": "Progress created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT update progress
    def put(self, request, *args, **kwargs):
        progress_id = request.data.get("id")
        if not progress_id:
            return Response(
                {"error": "You must provide an ID to update progress"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            progress = Progress.objects.get(id=progress_id, user=request.user)
        except Progress.DoesNotExist:
            return Response(
                {"error": "Progress not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(progress, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Progress updated", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE progress
    def delete(self, request, *args, **kwargs):
        progress_id = request.data.get("id")
        if not progress_id:
            return Response(
                {"error": "You must provide an ID to delete progress"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            progress = Progress.objects.get(id=progress_id, user=request.user)
            progress.delete()
            return Response({"message": "Progress deleted"}, status=status.HTTP_200_OK)
        except Progress.DoesNotExist:
            return Response(
                {"error": "Progress not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
