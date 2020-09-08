import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")

def main():
    """
    This is the main entry point for the program.
    """
    # Create the queue of 'work'
    work_queue = queue.Queue()

    # Put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # Create some synchronous tasks
    tasks = [
        (task, "One", work_queue),
        (task, "Two", work_queue)
    ]

    # Run the tasks
    for t, n, q in tasks:
        t(n, q)

if __name__ == "__main__":
    main()


        for i in range(1):

            if int(self.coordinates[0]) < 0:
                sh.canvas.canvas.move(self.rect_id, 10, 0)
            elif int(self.coordinates[1]) < 0:
                sh.canvas.canvas.move(self.rect_id, 0, 10)
            elif int(self.coordinates[2]) > WIDTH:
                sh.canvas.canvas.move(self.rect_id, -10, 0)
            elif int(self.coordinates[3]) > HEIGHT:
                sh.canvas.canvas.move(self.rect_id, 0, -10)


    #    for item in prtl.list_of_portals:
    #        if self.coordinates == item.coordinates:
    #            sh.canvas.canvas.move(self.rect_id, rndt(-50, 50, 10), rndt(-50, 50, 10))




        for item in sp.list_of_pillares:
            #укалывание справа
            if self.coordinates[0] == item.coordinates[2] and self.coordinates[1] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 10, 0)
            #укалывание снизу
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[1] == item.coordinates[3] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 0, 10)
            #укалывание слева
            elif self.coordinates[1] == item.coordinates[1] and self.coordinates[2] == item.coordinates[0] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, -10, 0)
            #укалывание сверху
            elif self.coordinates[0] == item.coordinates[0] and self.coordinates[3] == item.coordinates[1] :
                self.damage(item.force)
                sh.canvas.canvas.move(self.rect_id, 0, -10)



        sh.canvas.root.after(30, self.checker_collide)
