def train_doors_message() -> str:
    """Return the platform announcement string."""
    return (
        ":bullettrain_front:請勿靠近車門, 請不要靠近車門, "
        "please stand back from the train doors"
    )


if __name__ == "__main__":
    print(train_doors_message())
