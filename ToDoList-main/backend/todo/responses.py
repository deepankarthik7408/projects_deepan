from rest_framework.response import Response


UNAUTHORIZED_401 = Response({'Error': 'Unauthorized'}, 401)
