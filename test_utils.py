from coach.utils import fetch_and_parse, generate_learning_strategies

def test():
    test_url = 'https://interviewing.io/questions/two-sum'  # Replace with a URL of your choice
    content = fetch_and_parse(test_url)
    strategies = generate_learning_strategies(content)
    print("Extracted Content:\n", content)
    print("\nGenerated Strategies:\n", strategies)

if __name__ == "__main__":
    test()
