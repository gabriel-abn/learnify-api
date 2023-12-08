from faker import Faker
from faker.providers import internet, person, profile

from src.domain.entities import UserProps

faker = Faker()

faker.add_provider(person)
faker.add_provider(profile)
faker.add_provider(internet)


def make_fake_user(
    username: str = faker.user_name(),
    email: str = faker.free_email(),
    password: str = "ABCabc1!",
    first_name: str = faker.first_name(),
    last_name: str = faker.last_name(),
    role: str = faker.random_element(elements=("ADMIN", "STUDENT", "INSTRUCTOR")),
) -> UserProps:
    """Return a fake User object."""
    init_props: UserProps = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
    }

    return init_props
