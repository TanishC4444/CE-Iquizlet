import json
import re

def parse_quiz_file(filename):
    """
    Parse a text file containing quiz questions and convert to JSON format.
    """
    quiz_data = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content by separator lines or articles
    sections = re.split(r'={50,}', content)
    
    current_link = None
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        lines = section.split('\n')
        
        # Extract link if present
        for line in lines:
            if line.startswith('Link:'):
                current_link = line.replace('Link:', '').strip()
                break
        
        # Find questions in this section
        questions = []
        current_question = None
        current_choices = []
        current_correct = None
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if this is a question line (starts with Q1., Q2., etc.)
            question_match = re.match(r'^Q\d+\.\s*(.+)', line)
            if question_match:
                # Save previous question if exists
                if current_question and current_choices and current_correct:
                    questions.append({
                        'text': current_question,
                        'choices': current_choices,
                        'correctAnswer': current_correct,
                        'link': current_link or ""
                    })
                
                # Start new question
                current_question = question_match.group(1)
                current_choices = []
                current_correct = None
                
                # Look for choices on following lines
                j = i + 1
                while j < len(lines):
                    choice_line = lines[j].strip()
                    choice_match = re.match(r'^([A-D])\.\s*(.+)', choice_line)
                    if choice_match:
                        letter = choice_match.group(1)
                        text = choice_match.group(2)
                        current_choices.append({
                            'letter': letter,
                            'text': text
                        })
                        j += 1
                    elif choice_line.startswith('Correct Answer:'):
                        # Extract correct answer
                        correct_match = re.search(r'Correct Answer:\s*([A-D])', choice_line)
                        if correct_match:
                            current_correct = correct_match.group(1)
                        break
                    elif choice_line == '' or choice_line.startswith('Q'):
                        break
                    else:
                        j += 1
                
                i = j - 1
            
            i += 1
        
        # Don't forget the last question in the section
        if current_question and current_choices and current_correct:
            questions.append({
                'text': current_question,
                'choices': current_choices,
                'correctAnswer': current_correct,
                'link': current_link or ""
            })
        
        # Add all questions from this section to the main list
        quiz_data.extend(questions)
    
    return quiz_data

def save_as_json(quiz_data, output_filename):
    """
    Save quiz data as JSON file.
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(quiz_data, file, indent=4, ensure_ascii=False)

def save_as_js_variable(quiz_data, output_filename):
    """
    Save quiz data as JavaScript variable.
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write('const quizData = ')
        json.dump(quiz_data, file, indent=4, ensure_ascii=False)
        file.write(';')

def main():
    input_file = 'input.txt'  # Change this to your input file name
    
    try:
        # Parse the quiz file
        quiz_data = parse_quiz_file(input_file)
        
        print(f"Parsed {len(quiz_data)} questions from {input_file}")
        
        # Save as JSON
        save_as_json(quiz_data, 'quiz_output.json')
        print("Saved as quiz_output.json")
        
        # Save as JavaScript variable (like in your second document)
        save_as_js_variable(quiz_data, 'quiz_output.js')
        print("Saved as quiz_output.js")
        
        # Print first question as example
        if quiz_data:
            print("\nExample of first question:")
            print(json.dumps(quiz_data[0], indent=2))
            
    except FileNotFoundError:
        print(f"Error: Could not find file '{input_file}'")
        print("Please make sure the input file exists in the same directory as this script.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()