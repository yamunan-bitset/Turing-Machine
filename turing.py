#!/usr/bin/python3

class TuringMachine:
	def __init__(self, instructions, start_length=3):
		self.rules = instructions
		self.number_of_rules = len(self.rules)
		self.number_sequence = [0, 0, 0]
		for i in range(2, start_length):
			self.number_sequence.append(0)
		self.current_pos = 1
		self.current_rule = 0
		self.x = self.number_sequence[self.current_pos]
		self.done = False
		self.number_of_moves = 1

	def next_move(self):
		assert self.done == False
		try:
			match self.rules[self.current_rule][self.x][0]:
				case '0':
					self.number_sequence[self.current_pos] = 0
				case '1':
					self.number_sequence[self.current_pos] = 1

			match self.rules[self.current_rule][self.x][1]:
				case 'L':
					self.current_pos -= 1
					if self.current_pos < 0:
						self.number_sequence.insert(0, 0)
						self.current_pos = 0
				case 'R':
					self.current_pos += 1
					if len(self.number_sequence) <= self.current_pos:
						self.number_sequence.append(0)
						self.current_pos = len(self.number_sequence) - 1

			self.current_rule = ord(self.rules[self.current_rule][self.x][2]) - 65
			assert 0 <= self.current_rule <= 25

		except (ValueError, AssertionError) as _:
			self.done = True
			return "HLT!! Turing machine halted."	
	
		self.x = self.number_sequence[self.current_pos]
		self.number_of_moves += 1

		return self.get_state()

	def get_state(self):
		return self.number_sequence, self.current_pos, self.current_rule
	
	def __repr__(self):
		try:
			return f"Step {self.number_of_moves}: {self.number_sequence}, Position: {self.current_pos}, Rule: {self.rules[self.current_rule][self.x]}"
		except IndexError:
			return f"Turing machine halted after: Step {self.number_of_moves}"

if __name__ == "__main__":
	rules = [
            ['1RB', '1LB'],
            ['1LA', '0LC'],
            ['---', '1LD'],
            ['1RD', '0RA']
        ] # Should halt after BB(4)=107 steps
	tm = TuringMachine(rules)

	#print("Step 0:", (tm.number_sequence, tm.current_pos, tm.current_rule))
	print(repr(tm))
	halted = False
	while not halted:
		x = tm.next_move()
		print(repr(tm))
		if x == "HLT!! Turing machine halted.":
			halted = True