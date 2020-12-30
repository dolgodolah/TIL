/**
 * 자료형에 상관없이 값이 비어있는지 확인
 * 
 * @param value - 타겟 밸류
 * @returns true or false
 */
function isEmpty(value) {
	if (value == null || value == "" || value == undefined || (value != null && typeof value == "object" && !Object.keys(value).length)) {
		return true;
	}

	return false;
}

/**
 * 문자열의 마지막 문자의 종성을 반환
 * 
 * @param str - 타겟 문자열
 * @returns 문자열의 마지막 문자의 종성
 */
function charToUnicode(str) {
	return (str.charCodeAt(str.length - 1) - 0xAC00) % 28;
}

/**
 * 필드1, 필드2의 값이 다르면 해당 필드2로 focus한 뒤에 메시지 출력
 * 
 * @param field1 - 타겟 필드1
 * @param field2 - 타겟 필드2
 * @param fieldName - 필드 이름
 * @returns 메시지
 */
function equals(field1, field2, fieldName) {
	if (field1.value === field2.value) {
		return true;
	} else {
		/* alert 메시지 */
		var message = "";
		/* 종성으로 을 / 를 구분 */
		if (charToUnicode(fieldName) > 0) {
			message = fieldName + "이 일치하지 않습니다.";
		} else {
			message = fieldName + "가 일치하지 않습니다.";
		}
		field2.focus();
		alert(message);
		return false;
	}
}

/**
 * field의 값이 올바른 형식인지 체크 (정규표현식 사용)
 * 
 * @param field - 타겟 필드
 * @param fieldName - 필드 이름 (null 허용)
 * @param focusField - 포커스할 필드 (null 허용)
 * @returns 메시지
 */
function isValid(field, fieldName, focusField) {

	if (isEmpty(field.value) == true) {
		/* 종성으로 조사(을 또는 를) 구분 */
		var message = (charToUnicode(fieldName) > 0) ? fieldName + "을 확인해 주세요." : fieldName + "를 확인해 주세요."; 
		field.focus();
		alert(message);
		return false;
	}

	return true;
}

/**
 * 둘 중 비어있지 않은 value를 반환
 * 
 * @param value1 - 타겟 밸류1
 * @param value2 - 타겟 밸류2
 * @returns 비어잇지 않은 vlaue
 */
function nvl(value1, value2) {
	return (isEmpty(value1) == false ? value1 : value2);
}