package com.example.stream.stream;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.*;

@SpringBootTest
class StreamApplicationTests {

	/*
	 Stream 은 중간 작업(Stream<T>를 반환)과 터미널 작업(타입이 정의된 결과를 반환)으로 나뉜다.
	 */

	@Test
	void iterator_반복() {
		List<String> list = Arrays.asList("apple", "banana", "cacao", "coffee");

//		for (String string : list) {
//			if (string.contains("a")) {
//				return true;
//			}
//		}
//		위 코드를 아래와 같이 한줄로 줄일 수 있다.
		boolean isExist = list.stream().anyMatch(element -> element.contains("a"));
		assertThat(isExist).isEqualTo(true);
	}

	@Test
	void filter_필터링() {
		List<String> list = Arrays.asList("apple", "banana", "cacao", "coffee");

		// filter() 메소드는 조건에 만족하는 스트림 요소들을 선택할 수 있도록 해준다.
		Stream<String> result = list.stream().filter(element -> element.contains("a"));
		assertThat(result.count()).isEqualTo(3);
	}

	@Test
	void map_매핑() {
		class Member {
			private String name;
			private List<String> favorites;

			public String getName() {
				return name;
			}

			public Member(String name, List<String> favorites) {
				this.name = name;
				this.favorites = favorites;
			}
		}

		List<Member> members = Arrays.asList(
				new Member("홍길동", Arrays.asList("apple", "banana")),
				new Member("심청이", Arrays.asList("coffee"))
		);

		// map() 메소드는 기존 요소에 특정 메소드를 적용하여 변환하고 변환된 새 요소를 스트림으로 수집할 수 있도록 해준다.
		Stream<String> stream = members.stream().map(member -> member.getName());
		List<String> result = stream.collect(Collectors.toList());

		List<String> expected = Arrays.asList("홍길동", "심청이"); // [홍길동, 심청이]

		assertThat(result).isEqualTo(expected);
	}

	@Test
	void flatMap_매핑() {
		class Member {
			private String name;
			private List<String> favorites;

			public List<String> getFavorites() {
				return favorites;
			}

			public Member(String name, List<String> favorites) {
				this.name = name;
				this.favorites = favorites;
			}
		}

		// Member 클래스에는 favorites 라는 List<String> 타입의 필드가 있다.
		List<Member> members = Arrays.asList(
				new Member("홍길동", Arrays.asList("apple", "banana")),
				new Member("심청이", Arrays.asList("coffee"))
		);

		// flatMap()은 favorites 필드의 모든 요소들을 추출하여 새로운 스트림 결과를 만들어 준다.
		Stream<String> stream = members.stream()
				.flatMap(member -> member.getFavorites().stream());
		List<String> result = stream.collect(Collectors.toList());

		List<String> expected = Arrays.asList("apple", "banana", "coffee");

		assertThat(result).isEqualTo(expected);
	}

	// 터미널 작업(타입이 정의된 결과를 반환)
	@Test
	void match_매치() {
		List<String> list = Arrays.asList("apple", "banana", "cacao");

		// 요소들 중 "b"를 포함하고 있는 요소가 있는지 판단한다.
		boolean isValid = list.stream().anyMatch(element -> element.contains("b"));
		assertThat(isValid).isEqualTo(true);

		// 모든 요소들이 "a"를 포함하고 있는지 판단한다.
		isValid = list.stream().allMatch(element -> element.contains("a"));
		assertThat(isValid).isEqualTo(true);

		// 모든 요소들이 "q" 포함하지 않고 있는지 판단한다.
		isValid = list.stream().noneMatch(element -> element.contains("q"));
		assertThat(isValid).isEqualTo(true);

		isValid = list.stream().noneMatch(element -> element.contains("a"));
		assertThat(isValid).isEqualTo(false);
	}

	@Test
	void distinct_중복제거() {
		List<String> list = Arrays.asList("apple", "banana", "cacao", "apple", "banana");

		// distinct() 는 스트림 요소들의 중복을 제거해준다.
		Stream<String> distinct = list.stream().distinct();
		assertThat(distinct.count()).isEqualTo(3);
	}

	@Test
	void Stream_참조할_때_주의사항() {
		List<String> list = Arrays.asList("apple", "banana", "cacao", "coffee");

		// 스트림 요소들 중 "c"를 포함하는 요소들만 선택하는 중간 작업을 진행하고
		Stream<String> stream = list.stream().filter(element -> element.contains("c"));

		// 터미널 작업을 진행한다.
		Optional<String> anyElement = stream.findAny();

		assertThat(anyElement).isNotEmpty();
		assertThat(anyElement.get()).isEqualTo("cacao");

		/*
		이전에 터미널 작업을 호출한 후 동일한 참조를 재사용하려고 하면 IllegalStateException 을 던진다.
		즉, 스트림은 재사용할 수 없음을 기억하는 것이 매우 중요하다.
		 */
		assertThatThrownBy(() -> stream.findFirst()).isInstanceOf(IllegalStateException.class);

		/*
		따라서 이전 코드가 작동하기 위해서는 다음과 같이 수정을 해야한다.
		 */
		List<String> elements = list.stream()
				.filter(element -> element.contains("c"))
				.collect(Collectors.toList());
		Optional<String> any = elements.stream().findAny();
		assertThat(any).isNotEmpty();
		assertThat(any.get()).isEqualTo("cacao");

		Optional<String> first = elements.stream().findFirst();
		assertThat(first).isNotEmpty();
		assertThat(first.get()).isEqualTo("cacao");
	}

	@Test
	void 스트림_파이프라인() {
		/*
		스트림 그 자체는 가치가 없다. 사용자는 터미널 작업의 결과에 관심이 있다.
		스트림을 사용하는 정확하고 가장 편리한 방법은 중간 작업, 터미널 작업의 체인인 파이프라인을 사용하는 것이다.
		파이프라인? : 데이터 처리 단계의 출력이 다음 단계의 입력으로 이어지는 형태로 연결된 구조
		 */
		List<String> list = Arrays.asList("abc1", "abc2", "abc3");
		long result = list.stream()
				.skip(1)
				.map(element -> element.substring(0, 3))
				.count();

		assertThat(result).isEqualTo(2);
	}

	@Test
	void 실행_순서() {
		class Counter {
			private long count;

			public long getCount() {
				return count;
			}

			private void wasCalled() {
				count++;
			}

			private void initCount() {
				count = 0;
			}
		}

		Counter counter = new Counter();
		List<String> list = Arrays.asList("abc1", "abc2", "abc3");

		/*
		아래 코드를 실행되면 카운터 값이 3만큼 증가할 것이다.
		즉, 비싼 map() 메소드를 3번 호출했지만, size 는 1이다.
		3번 중 2번은 이유 없이 값 비싼 map() 메소드를 호출하게 된 것이다.
		 */
		long size1 = list.stream().map(element -> {
			counter.wasCalled();
			return element.substring(0, 3);
		}).skip(2).count();

		assertThat(counter.getCount()).isEqualTo(3);


		/*
		skip()과 map()의 순서를 바꿨다.
		비싼 map() 메소드의 호출은 1번으로 줄었고, 구하고자 했던 size 는 전과 동일 하다.
		 */
		counter.initCount();
		long size2 = list.stream().skip(2).map(element -> {
			counter.wasCalled();
			return element.substring(0, 3);
		}).count();

		assertThat(counter.getCount()).isEqualTo(1);
		assertThat(size1).isEqualTo(size2);
	}
}
