import npyscreen, curses


class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())


class MainForm(npyscreen.Form):
    def create(self):
        self.add(
            npyscreen.TitleText, name="Text:", value="Press Escape to quit application"
        )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = (
            self.exit_application
        )

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False


def main():
    TA = MyTestApp()
    TA.run()


if __name__ == "__main__":
    main()
