from src.mars_controller import Controller
from src.exceptions.ex_invalid_plateau_bounds import InvalidPlateauBounds
from src.exceptions.ex_collision import CollisionException
from src.exceptions.ex_rover import InvalidRover
from src.exceptions.ex_plateau import PlateauException
import src.constants as c
import re

landing_pattern = re.compile("\d+\s+\d+\s+[nsew]", re.IGNORECASE)


def init_msg():
    """
    Print initial message with some instructions
    :return:
    """
    print " \n"
    print " == Welcome to the MARS src =="
    print "Here are some example of inputs: "
    print "Plateau:5 5"
    print "Rover1 Landing:1 2 N"
    print "Rover1 Instructions:LMLMLMLMM"
    print "Rover2 Landing:3 3 E"
    print "Rover2 Instructions:MMRMMRMRRM"

    print " "
    print " Please, press: 'Enter' to check the rovers on Plateau"
    print " Please, type: 'quit' to exit Mars."

    print " \n"


def output(rover_name, rover_obj):
    """
    :param rover_name: (str) rover name identifier
    :param rover_obj: (obj) rover object itself
    :return:
    """
    if rover_obj and rover_obj.is_landed():
        print '{}:{} {} {}'.format(rover_name.capitalize(), rover_obj.x_pos,
                                   rover_obj.y_pos, rover_obj.heading.upper())

    else:
        print 'No rover to report'
        print '\n'


def resume_rovers(dict_rovers):
    """
    :param dict_rovers: dict containing rovers identified by names
    :return:
    """
    print "\n## OUTPUT ##"

    if len(dict_rovers) > 0:
        for name, rover in dict_rovers.iteritems():
            output(name, rover)
    else:
        print 'No rover to report'
        print '\n'


def plateau_input_handle(command_parts, ctrl):
    """
    :param command_parts: (list) containing the plateau command divided into
                          suffix and prefix
    :param ctrl: (obj) Controller object
    :return:
    """
    # Remove empty spaces
    if ctrl:
        command_parts = map(str.strip, command_parts)
        parameters = command_parts[1].split(' ')

        # Filter params_list to get only numeric digits.
        dimension_parameters = filter(
            lambda param: str.isdigit(param), parameters)

        if len(dimension_parameters) == 2:
            x = int(dimension_parameters[0])
            y = int(dimension_parameters[1])

            try:
                ctrl.set_plateau(x, y)
            except PlateauException as ex:
                print ex.msg

        else:
            print "Plateau invalid arguments {}.".format(command_parts)


def is_landing_param_valid(landing_params):
    """
    :param landing_params: (str) Expected to be similar to '5 5 n'
    :return: Bool
    """
    return landing_pattern.match(landing_params) is not None


def landing_input_handle(command_parts, ctrl):
    """
    :param command_parts: (list) containing the landing command divided into
                          suffix and prefix.
    :param ctrl: (obj) Controller object
    :return:
    """
    try:
        if ctrl and ctrl.plateau is None:
            raise ValueError("Plateau is required before "
                             "execute instructions.")
        elif command_parts:
            # Split string ex: '5 5 n' to handle easily the params
            name = command_parts[0].split(' ')[0]
            command_parts = map(str.strip, command_parts)

            if is_landing_param_valid(command_parts[1]):
                args = command_parts[1].split(' ')
                try:
                    ctrl.land_rover(x=int(args[0]), y=int(args[1]),
                                    heading=args[2],  name=name)
                except (InvalidPlateauBounds, ValueError,
                        CollisionException) as e:
                    print e

            else:
                print "Landing invalid arguments. {}".format(command_parts)
    except (InvalidPlateauBounds, ValueError, CollisionException) as ex:
        print ex


def instruction_input_handle(command_parts, ctrl):
    """
    :param command_parts: (list) containing the instructions command divided
                          into suffix and prefix.
    :param ctrl: (obj) Controller object
    :return:
    """

    try:
        if ctrl and ctrl.plateau is None:
            raise ValueError("Plateau is required before execute "
                             "instructions.")

        name = command_parts[0].split(' ')[0]
        instructions = command_parts[1]

        ctrl.instructions(name, instructions)

    except (ValueError, InvalidRover, CollisionException) as ex:
        print ex


def main():
    command = ''
    quit = 'quit'
    report = ''

    ctrl = Controller(plateau=None)

    init_msg()

    try:
        while command.strip() != quit:
            command = raw_input()

            # Remove whitespaces, put command to lower case and
            # break it into prefix (ex: plateau, landing, instruction)
            # and suffix ( params ex: '1 2 N', 'LMLMLMLMM')
            command_parts = command.strip().lower().split(':')

            if len(command_parts) == 2:
                # Plateau dimensions setting
                # ex: 'plateau: 5 5'
                if command_parts[0].endswith(c.PLATEAU):
                    plateau_input_handle(command_parts, ctrl)

                elif command_parts[0].endswith(c.LANDIND):
                    landing_input_handle(command_parts, ctrl)

                elif command_parts[0].endswith(c.INSTRUCTIONS):
                    instruction_input_handle(command_parts, ctrl)

            elif command == report:
                resume_rovers(ctrl.dict_rover)

            elif command.strip() != quit:
                print "'{}' is not a valid command. " \
                      "Please check the syntax.".format(command)
        resume_rovers(ctrl.dict_rover)
        print "bye :)"
    except EOFError:
        pass


if __name__ == "__main__":
    main()
