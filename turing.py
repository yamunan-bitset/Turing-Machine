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
		
		try:
			self.current_rule = int(self.rules[self.current_rule][self.x][2])
		except ValueError:
			self.done = True
			return "HLT!! Turing machine halted."
	
		self.x = self.number_sequence[self.current_pos]
		self.number_of_moves += 1

		return self.number_sequence, self.current_pos, self.current_rule


if __name__ == "__main__":
	# Example usage
	#rules = [['1R1', '1R2'], ['0R2', '1L0'], ['HLT', '0L1']] # should halt after 3 steps
	#rules = [['1R1', '1R2'], ['0R2', '1L0'], ['HLT', '0L1']] # should halt after 3 steps
	#rules = [['1R1', '1R2'], ['0R2', '1L0'], ['HLT', '0L1']] # should halt after 3 steps
	'''rules = [
		['1R1', '1L1'],
		['1L0', '1RH']
	] # Should halt after 6 steps'''
	#rules = [['1R1', '1L1'], ['1L2', '0L0'], ['1R3', '1L0'], ['1R0', 'HLT']] 
	rules = [
            ['1R1', '1L1'],
            ['1L0', '0L2'],
            ['1RH', '1L3'],
            ['1R3', '0R0']
        ] # Should halt after BB(4)=107 steps
	tm = TuringMachine(rules)

	print("Step 0:", (tm.number_sequence, tm.current_pos, tm.current_rule))
	halted = False
	while not halted:
		x = tm.next_move()
		print(f"Step {tm.number_of_moves}: {x}")
		if x == "HLT!! Turing machine halted.":
			halted = True