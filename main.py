from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n')
    #내용을 불러오려면 w 모드가 아닌 r 모드 필요, 변수명 통일
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
            #\\\\일 때 원하는 대로 출력됨
        if '/' in file or '"' in file:
            #조건문의 정확하지 않은 동작 정리
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"'
    #잘못된 template 수정
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)
        #process_file(german_file)은 german_file에 처리되어야 함함

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
        #잘못된 template 순서 수정
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        #새로 만들어야하니까 r 모드가 아닌 w 모드 필요
        for file in file_list:
            f.write(file + '\n')
            #file이 없으면 공백만 나오므로 수정
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    #잘못된 함수 사용 수정

    write_file_list(processed_file_list, path+'concated.json')
