import requests as req
import json as json


class User:
    def __init__(
        self, id: str, first_name: str, last_name: str, email: str, avatar: str
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.avatar = avatar


class UserJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=UserJSONDecoder.hook, *args, **kwargs)

    @staticmethod
    def hook(user_json):
        return User(
            user_json["id"],
            user_json["first_name"],
            user_json["last_name"],
            user_json["email"],
            user_json["avatar"],
        )


def get_users() -> list[User] | None:
    try:
        reply = req.get("https://reqres.in/api/users")
    except req.RequestException:
        print("Communication Error")
    else:
        if not reply.ok:
            print("Error when fetching users.")
            return

        users_json = reply.json()
        if not users_json:
            return

        users = [
            json.loads(str(user).replace("'", '"'), cls=UserJSONDecoder)
            for user in users_json["data"]
        ]
        return users


def print_users(users: list[User]):
    for user in users:
        print(f"({user.id}) {user.first_name} {user.last_name}: {user.email}")


def download_avatars(users: list[User]):
    for user in users:
        avatar = req.get(user.avatar, stream=True)
        # if avatar.ok:
        #     with open("avatars/", "wb") as f:
        #         avatar.raw.decode_
        print(avatar.links)


def main():
    users = get_users()
    if not users:
        return

    print_users(users)
    download_avatars(users)


if __name__ == "__main__":
    main()
