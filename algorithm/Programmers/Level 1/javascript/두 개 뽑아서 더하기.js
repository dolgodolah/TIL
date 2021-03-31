// array.indexOf(element)는 array에서 element의 인덱스를 반환한다. 해당 element가 없으면 -1을 반환한다.
// array.sort()는 유니코드 기준 정렬(사전식 정렬), 수의 오름차순 정렬을 하기 위해서는 sort((a,b)=>a-b)를 해야한다.

function solution(numbers) {
    var answer = []
    for (var i = 0; i < numbers.length - 1; i++) {
        for (var j = i + 1; j < numbers.length; j++) {
            if (answer.indexOf(numbers[i] + numbers[j]) == -1) {
                answer.push(numbers[i] + numbers[j]);
            }
        }
    }
    answer.sort((a, b) => a - b);
    return answer;
}
console.log(solution([5, 0, 2, 7]));