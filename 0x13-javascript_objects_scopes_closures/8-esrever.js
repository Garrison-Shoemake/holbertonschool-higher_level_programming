#!/usr/bin/node
exports.esrever = function (list) {
  const oldlist = list;
  const newlist = [];
  for (let i = oldlist.length - 1; i >= 0; i--) {
    newlist.push(oldlist[i]);
  }
  return newlist;
};
