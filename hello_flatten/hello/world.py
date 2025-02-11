from loguru import logger
from pydantic import BaseModel

class Greeting(BaseModel):
    name: str
    message: str = "Hello"

    def format(self) -> str:
        # Format greeting with name
        return f"{self.message}, {self.name}!"

def say_hello(name: str = "World") -> str:
    # Create and return formatted greeting
    greeting = Greeting(name=name)
    logger.info(f"Generating greeting for {name}")
    return greeting.format()

def main():
    # Example usage
    result = say_hello("Developer")
    logger.info(result)
    return result

if __name__ == "__main__":
    main()
