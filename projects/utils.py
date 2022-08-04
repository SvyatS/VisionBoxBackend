def upload_path_render(instance, filename):
    return f'static/project-{instance.room.project.code}/room-{instance.room.id}/renders/{filename}'


def upload_path_panorama(instance, filename):
    return f'static/project-{instance.room.project.code}/room-{instance.room.id}/panoramas/{filename}'
