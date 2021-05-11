Board 클래스
```java
package test02;

public class Board {
	
	private String title;
	private String author;
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	@Override
	public String toString() {
		return "Board [title=" + title + ", author=" + author + "]";
	}	
}

```


for-each 사용
```java
package test02;

import java.util.ArrayList;
import java.util.List;

public class ForEach {
	

	public static void main(String[] args) {
		
		/*
		 * 기존 for문은 인덱스를 통해 배열이나 리스트에 접근을 하기 때문에 IndexOutOfBoundsException의 가능성이 있다.
		 * for-each는 이러한 오류 가능성을 줄이고 가독성을 높일 수 있다.
		 * 그러나 배열의 특정 원소 값을 수정할 수 없다. (Only read)
		 */
		String names[] = {"딸기", "수박", "참외", "포도"};
		for (String s : names) {
			System.out.println(s);
		}
		
		List<Board> boards = new ArrayList<>();
		
		Board board1 = new Board();
		boards.add(board1);
		Board board2 = new Board();
		boards.add(board2);
		Board board3 = new Board();
		boards.add(board3);
		
		/*
		 * 인덱스에 따른 처리를 해야할 때는 기존 for문을 통해 접근한다.
		 */
		for (int i=0; i<boards.size(); i++) {
			Board board = boards.get(i);
			board.setTitle((i+1)+"번째 게시글");
			board.setAuthor((i+1)+"번째 작성자");
		}
		
		for (Board b:boards) {
			System.out.println(b.toString());
		}

	}

}

```