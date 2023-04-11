import 'dart:io';

void main() {
  String? s = stdin.readLineSync();
  List<String> arr = <String>[s![0]];
  String tmp = '';

  for (var a in s.split('')) {
    tmp += a;
    if (!arr.contains(tmp)) {
      arr.add(tmp);
      tmp = '';
    }
  }

  arr.add(tmp);

  print(arr);
}
