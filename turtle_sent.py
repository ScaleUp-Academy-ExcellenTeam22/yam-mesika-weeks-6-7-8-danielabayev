import PostOffice


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter', 'Daniel')
    post_office = PostOffice.PostOffice(users)
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    message_id = post_office.send_message(
        sender='Newman',
        recipient='Mr. Peanutbutter',
        message_body='Hello, Mr. Peanutbutter.',
    )
    message_id = post_office.send_message(
        sender='Newman',
        recipient='Daniel',
        message_body='Hello, Daniel.',
    )
    message_id = post_office.send_message(
        sender='Newman',
        recipient='Daniel',
        message_body='my message.',
    )
    print(f"Successfuly sent message number {message_id}.")
    print(post_office.boxes['Mr. Peanutbutter'])
    print(post_office.boxes['Newman'])
    print(post_office.boxes['Daniel'])
    print(post_office.read_inbox('Daniel', 1))
    print(post_office.read_inbox('Daniel', 1))
    print(post_office.read_inbox('Daniel', 1))


if __name__ == "__main__":
    show_example()
