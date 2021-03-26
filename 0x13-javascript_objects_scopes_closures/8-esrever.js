#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let size = list.length - 1;

  for (; size >= 0; size--) {
    reversedList.push(list[size]);
  }
  return reversedList;
};
