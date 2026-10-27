Django REST Framework(DRF)

permissions.py
- class AllowAny :- Anyone can access the APIs.
- class IsAuthenticated :- Only logged-in users can access the APIs.
- class IsAdminUser :- Only Admin/Staff users can access the APIs.
- class IsAuthenticatedOrReadOnly :- Anyone can read, only Authenticated users can make changes

Example:-

    from rest_framework.permissions import IsAuthenticated
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class DemoView(APIView):

        permission_classes=[IsAuthenticated]

        def get(self,request):
            return Response({'msg':"HELLO"})

 