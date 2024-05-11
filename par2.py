import nltk
from nltk import Tree

from par3 import demo

# Read the file
file_path = "/Users/achraffaress/Documents/GitHub/Pav_project/formatted_sentences.txt"
with open(file_path, "r") as file:
    tree_strings = file.readlines()

# Remove newline characters
tree_strings = [tree_string.strip() for tree_string in tree_strings]

def extract_rules(tree_string):
    tree = Tree.fromstring(tree_string)
    return tree.productions()

def combine_grammar(trees):
    rules_dict = {}  # Dictionary to hold rules by left-hand side
    for tree_string in trees:
        rules = extract_rules(tree_string)
        for rule in rules:
            lhs = str(rule.lhs())
            rhs = str(rule.rhs())
            if lhs in rules_dict:
                rules_dict[lhs].add(rhs)
            else:
                rules_dict[lhs] = {rhs}
    return rules_dict

def format_grammar(rules_dict):
    grammar_str = ""
    for lhs, rhs_set in sorted(rules_dict.items()):
        if lhs == "''" or lhs == "``":
            continue
        rhs_str = " | ".join(sorted(rhs_set)).replace("(", "").replace(")", "").replace(",", "").replace("``", "")  # Join all right-hand sides with ' | ' and remove parentheses
        grammar_str += f"  {lhs} -> {rhs_str}\n"
    return grammar_str

# Read tree strings from file and combine rules
combined_rules = combine_grammar(tree_strings)

# Format the grammar as a single string
demo_grammar = format_grammar(combined_rules)

# Print the formatted grammar
#print(demo_grammar)
demo(grammer_input= demo_grammar)