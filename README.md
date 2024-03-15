# Mindmap Generator

This Python program generates a visual mind map from a YAML configuration file.

## Description
The program takes two arguments:
* Title: The title of the mind map.
* Filename: The path to a YAML file containing the mind map structure.

The YAML file should use nested lists and dictionaries to represent the nodes and branches of the mind map.
The program then uses the pydot library to generate a graph representation of the mind map and saves it as a PNG image.

## Example
### mindmap.yaml:
```yaml
Main Topic:
  - Subtopic 1:
    - Sub-subtopic 1
    - Sub-subtopic 2
  - Subtopic 2
  - Subtopic 3:
    - Sub-subtopic 3
```

### Command:
`python mindmap.py "My Mind Map" mindmap.yaml`

This will generate a file named mindmap.yaml.png containing a visual representation of the mind map.
