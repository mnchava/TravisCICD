import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username="me")
    assert me.is_superuser


@pytest.fixture
def user_2(db):
    user = User.objects.create_user("test-user2")
    print("create-user2")
    return user


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user

    return create_app_user


@pytest.fixture
def new_user(db, new_user_factory):
    return new_user_factory("Test_user", "password", "MyName")


@pytest.fixture
def new_staff_user(db, new_user_factory):
    return new_user_factory("Test_user", "password", "MyName", is_staff="True")
