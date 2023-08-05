import 'dart:io';

void main() {
  String? s = stdin.readLineSync();
  List<String> arr = <String>[s![0]];

  if (s.length == 1) {
    print(s);
  } else {
    int p = 1;

    while (p < s.length) {
      int c = 0;

      while (p + c < s.length && arr.contains(s.substring(p, p + c))) {
        c += 1;
      }

      arr.add(s.substring(p, p + c));
      p += c;
    }

    arr.removeAt(1);
    print(arr.join(' '));
  }
}
