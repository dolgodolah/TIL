
```java
public class 컬렉션 {

	public static void main(String[] args) {
		
		/*
		 * Collection은 자바에서 자료 구조를 구현한 클래스들을 말하는데, 동일한 데이터 타입을 가진 것들을 모은 집합입니다.
		 */
		
		// 1. List (ArrayList, LinkedList, Vector)
		ArrayList<String> list = new ArrayList<>();
		list.add("사과");
		list.add("딸기");
		list.add(1,"수박");
		list.remove("사과");
		
		System.out.println(list); //[수박, 딸기]
		
		
		

		// 2. Set (HashSet, TreeSet, LinkedHashSet)
		
		// (1) HashSet : 해시테이블로서 성능이 가장 우수하지만 입력 순서를 보장하지 않습니다.
		HashSet<String> hashSet = new HashSet<>();
		hashSet.add("Milk");
		hashSet.add("Bread");
		hashSet.add("Butter"); // 중복 허용하지 않습니다.
		hashSet.add("Cheese");
		hashSet.add("Butter");
		System.out.println(hashSet); // [Butter, Cheese, Milk, Bread]
		
		
		// (2) LinkedHashSet : HashSet보다 느리지만 입력된 순서를 보장합니다.
		LinkedHashSet<String> linkedHashSet = new LinkedHashSet<>();
		linkedHashSet.add("Milk");
		linkedHashSet.add("Bread");
		linkedHashSet.add("Butter");
		linkedHashSet.add("Cheese");
		System.out.println(linkedHashSet); // [Milk, Bread, Butter, Cheese]
		
		
		// (3) TreeSet : 성능면에서 HashSet보다 떨어지나 정렬이 된 Set을 얻을 수 있습니다.
		TreeSet<String> treeSet = new TreeSet<>();
		treeSet.add("Milk");
		treeSet.add("Bread");
		treeSet.add("Butter");
		treeSet.add("Cheese");
		System.out.println(treeSet); // [Bread, Butter, Cheese, Milk] 사전순으로 정렬 된 것을 볼 수 있습니다.
		
		
		
		
		
		// 3. Queue (PriorityQueue, Deque)
		PriorityQueue<String> pq = new PriorityQueue<String>();
		pq.add("Milk");
		pq.add("Bread");
		pq.add("Butter");
		pq.add("Cheese");
		for (String s : pq) {
			System.out.println(s); // 최상단의 순서만 유지합니다.
		}
		System.out.println("원소 삭제");
		while(!pq.isEmpty()) {
			System.out.println(pq.remove()); // Bread->Butter->Cheese->Milk 사전순대로 제거되는걸 볼 수 있습니다.
		}
		
		/*
		 *  remove()와 poll()의 차이는 예외처리 여부입니다.
		 *  queue가 비어있을 때 remove()를 하면 예외처리가 되지만
		 *  poll()을 하면 null 을 반환합니다.
		 */
		
		
		
		
		
		// 4. Map (HashMap, TreeMap, LinkedHashMap)
		Map<Integer, Student> map = new HashMap<Integer, Student>();
		map.put(1, new Student("김규범",25));
		map.put(2, new Student("홍길동",23));
		map.put(3, new Student("유재석",45));
		
		System.out.println(map); //{1=Student [name=김규범, age=25], 2=Student [name=홍길동, age=23], 3=Student [name=유재석, age=45]}
		map.remove(2);
		System.out.println(map); //{1=Student [name=김규범, age=25], 3=Student [name=유재석, age=45]}
		
		for(Map.Entry<Integer, Student> m : map.entrySet()) {
			System.out.println(m);
		}
		
		
		Map<String, Integer> m = new HashMap<String, Integer>();
		String[] words = {"a", "b", "c", "a", "d" ,"a", "b"};
		for (String s : words) {
//			if(!m.containsKey(s)) {
//				m.put(s, 1);
//			}else {
//				m.put(s, m.get(s)+1);
//			}
			m.put(s, (m.get(s)==null) ? 1 : m.get(s) + 1);
		}
		System.out.println(m);
	}

}
```


```java
class Student{
	String name;
	int age;
	
	public Student(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	@Override
	public String toString() {
		return "Student [name=" + name + ", age=" + age + "]";
	}	
}
```



## 참고
[자바에서 제공하는 컬렉션 프레임워크 구조](https://developer-youn.tistory.com/19?category=817604)
