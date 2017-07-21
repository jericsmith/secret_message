import os
import secret_message.utility


def descramble_message(message_path: str) -> None:

    if not os.path.exists(message_path):
        print(message_path + " does not exist")
        return None

    file_list = os.listdir(message_path)
    for f in file_list:
        alpha_list = []
        for c in f:
            if c.isdigit():
                continue
            alpha_list.append(c)

        source = os.path.join(message_path, f)
        target = os.path.join(message_path, ''.join(alpha_list))
        if not os.path.exists(source):
            continue

        if os.path.exists(target):
            secret_message.utility.delete_file(target)

        os.rename(source, target)

