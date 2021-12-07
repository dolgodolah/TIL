# nil

`nil?`은 해당 오브젝트가 nil인지를 판별하여 알려준다.

```ruby
nil.nil?
=> true

true.nil?
=> false

5.nil?
=> false

"".nil?
=> false

[].nil?
=> false
```

# empty

`string`, `array`, `hash`, `set에서 사용되는 메소드이다.

자료구조가 비어있거나 문자열 길이가 0일 때 true를 반환한다.

`nil`이나 `Integer`처럼 `empty` 메소드가 정의되지 않은 오브젝트에서 사용하면 `NoMethodError`가 발생한다.

```ruby
"".empty?
=> true

" ".empty?
=> false

"\t\n".empty?
=> false

[].empty?
=> true

{}.empty?
=> true

Set.new.empty?
=> true
```

# blank

모든 오브젝트에서 사용 가능하고, 문자열에서는 공백까지 전부 `true`로 리턴한다.

```ruby
"".blank?
=> true

" ".blank?
=> true

"\n\t".blank?
=> true

[].blank?
=> true

{}.blank?
=> true

Set.new.blank?
=> true

[nil].blank?
=> false

["", ""].blank?
=> false

person = {:firstName => "John", :lastName => "Doe"}
person.blank?
=> false
```

true, false, nil 값에 대해서는 조금 특이하다.

```ruby
true.blank?
=> false

false.blank?
=> true

nil.blank?
=> true
```

일부 오브젝트에서만 사용할 수 있어 `NoMethodError`의 가능성이 있는 `empty`보다는

모든 오브젝트에서 사용할 수 있고 whitespace까지 검사해주는 `blank`를 사용하는 것이 더 좋다. 

# present

`blank`의 반대이다.

```ruby
"".present?
=> false

" ".present?
=> false

[].present?
=> false

nil.present?
=> false

true.present?
=> true

false.present?
=> false

{}.present?
=> false

person = {:firstName => "John", :lastName => "Doe"}
person.present?
=> true

5.present?
=> true
```

# 결론

# 참조

[https://blog.appsignal.com/2018/09/11/differences-between-nil-empty-blank-and-present.html](https://blog.appsignal.com/2018/09/11/differences-between-nil-empty-blank-and-present.html)