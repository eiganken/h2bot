import re
import yaml
import database as db
import command as cmd


url_checker = re.compile(r"https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+")


def parse(message):
    if message.content.split(' ')[0] == '/echi':
        command_props = list(filter(lambda x: x != ' ', message.content.split(' ')))
        if len(command_props) == 1:
            return cmd.get_cmd_mannual()
        if cmd.is_include(command_props[1]):
            return cmd.run(command_props[1], command_props[2:])
        else:
            return "command error: {}? なんすか{}って？".format(command_props[1], command_props[1])

    else:
        if url_checker.match(message.content) is None:
            return None

        url_props = re.split('[:,/,?]', message.content)[3:]

        if url_props[0] == 'twitter.com':
            db.add_post(message.author, url_props[3], url_props[1])

def parse_test(message):
    if message.split(' ')[0] == '/echi':
        command_props = list(filter(lambda x: x != ' ' and x != '', message.split(' ')))
        if len(command_props) == 1:
            return cmd.get_cmd_mannual()
        if cmd.is_include(command_props[1]):
            return cmd.run(command_props[1], command_props[2:])
        else:
            return "command error: {}? なんすか{}って？".format(command_props[1], command_props[1])

    else:
        if url_checker.match(message) is None:
            return None

        url_props = re.split('[:,/,?]', message)[3:]

        if url_props[0] == 'twitter.com':
            db.add_post('test_user', url_props[3], url_props[1])