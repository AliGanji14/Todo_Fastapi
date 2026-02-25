from auth.jwt_auth import get_authenticate_user
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, Depends, Response, Request
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes
from users.routes import router as users_routes
from users.models import UserModel


tags_metadata = [
    {
        'name': 'tasks',
        'description': 'Operations related to task management',
        'externalDocs': {
            'description': 'More about tasks',
            'url': 'https://github.com/AliGanji14'
        }
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Application startup')
    yield
    print('Application shutdown')

app = FastAPI(title="Todo Application",
              description='this is a section for description',
              version="0.0.1",
              terms_of_service="http://example.com/terms/",
              contact={
                      "name": "Ali Ganji",
                      "url": "https://github.com/AliGanji14",
                      "email": "aliganji1309@gmail.com",
              },
              license_info={
                  "name": "MIT",
              }, lifespan=lifespan, openapi_tags=tags_metadata)

app.include_router(tasks_routes)
app.include_router(users_routes)


@app.post('/set-cookie')
def set_cookie(response: Response):
    response.set_cookie(key='test', value='something')
    return {'message': 'cookie has been set successfully.'}


@app.get('/get-cookie')
def set_cookie(request: Request):
    print(request.cookies.get('test'))
    return {'message': 'cookie has been set successfully.'}
