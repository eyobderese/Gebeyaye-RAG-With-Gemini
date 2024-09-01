from rag import (
    generate_text,
    process_query
)


def main():

    prompt = process_query("who is Eyob")

    response = generate_text(prompt)
    print(response)


if __name__ == "__main__":
    main()
