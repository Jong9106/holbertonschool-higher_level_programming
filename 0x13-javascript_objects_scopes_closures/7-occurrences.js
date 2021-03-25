#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let counter = 0;
  for (; i < list.length; i++) {
    if (searchElement === list[i]) {
      counter += 1;
    }
  }
  return counter;
};
