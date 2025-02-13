# Main functions
import os
from huggingface_hub import InferenceClient
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich import inspect
from dotenv import load_dotenv
from .utilz import green_box, blue_box, l_error, write_results_to_file_with_date


console = Console()
load_dotenv("src/.env")

# Models
hf_models = [
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    "meta-llama/Llama-3.2-1B-Instruct",
]


# Accessing the Qwen Model
def qwen15():
    os.system("clear")
    """
    Inference with DeepSeek AI's Qwen-1.5B Model
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    """

    model = hf_models[0]
    console.rule(f"{model}", style="blue")
    ask_query = Prompt.ask(
        "Enter your query",
        default="Explain cosmogenesis",
    )

    blue_box(
        f"""{model}
{ask_query}""",
        "Query",
    )

    try:
        client = InferenceClient(model=model, token=os.getenv("HFA"))
    except Exception as e:
        console.log(f"[bold red]Failed to initialize the inference client: {e}")
        return

    try:
        with console.status("[bold green]Generating response...\n", spinner="dots"):
            client_reply = client.text_generation(ask_query)

        rprint("[bold green]Response received!")
        green_box(client_reply, "success")

        write_results_to_file_with_date(model, ask_query, client_reply)

    except Exception as e:
        l_error(e)

    console.rule("END", style="blue")


# Accessing the llama model
def llam2():
    os.system("clear")
    """
    Inference with the LLAMA Client
    meta-llama/Llama-3.3-70B-Instruct
    """

    model = hf_models[1]
    console.rule(f"{model}", style="blue")
    ask_query = Prompt.ask(
        "Enter your query",
        default="Explain cosmogenesis",
    )

    blue_box(
        f"""{model}
{ask_query}""",
        "Query",
    )

    try:
        client = InferenceClient(
            model=model,
            token=os.getenv("HFA"),
        )
    except Exception as e:
        console.log(f"[bold red]Failed to initialize the inference client: {e}")
        return

    try:
        with console.status("[bold green]Generating response...\n", spinner="dots"):
            client_reply = client.text_generation(ask_query)

        rprint("[bold green]Response received!")
        green_box(client_reply, "success")

        write_results_to_file_with_date(model, ask_query, client_reply)

    except Exception as e:
        l_error(e)

    console.rule("END", style="blue")
